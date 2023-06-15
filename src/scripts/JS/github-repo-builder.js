const { Octokit } = require("@octokit/rest");
const fs = require("fs");
const path = require("path");

// Replace with your own GitHub authentication token
const octokit = new Octokit({ auth: "YOUR_AUTH_TOKEN" });

// Replace with the owner and name of the repository
const owner = "mmcg-treasury";
const repo = "usd";

// Get the contents of the repository
octokit.repos.getContent({ owner, repo, path: "" }).then(({ data }) => {
  // Loop through each file in the repository
  data.forEach((file) => {
    // Check if the file is a JavaScript file
    if (file.type === "file" && path.extname(file.name) === ".js") {
      // Check if the file exists locally
      if (!fs.existsSync(file.name)) {
        // Download the file from GitHub
        octokit.repos.getContent({ owner, repo, path: file.path }).then(({ data }) => {
          // Write the file to disk
          fs.writeFileSync(file.name, Buffer.from(data.content, "base64"));
          console.log(`File '${file.name}' created.`);
        });
      }
    }
  });
});
