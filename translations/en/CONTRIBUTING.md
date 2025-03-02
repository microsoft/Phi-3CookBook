# Contributing

This project encourages contributions and suggestions. Most contributions require you to sign a Contributor License Agreement (CLA), confirming that you have the rights to, and are granting us permission to, use your contribution. For more details, visit [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com).

When you submit a pull request, a CLA bot will automatically check if you need to sign a CLA and will update the PR accordingly (e.g., status check, comment). Just follow the bot's instructions. You only need to do this once for all repositories using our CLA.

## Code of Conduct

This project follows the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information, check out the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or reach out to [opencode@microsoft.com](mailto:opencode@microsoft.com) if you have any additional questions or comments.

## Cautions for creating issues

Please avoid opening GitHub issues for general support questions. The GitHub issue list is intended for feature requests and bug reports. This helps us focus on tracking real issues or bugs in the code while keeping general discussions separate.

## How to Contribute

### Pull Requests Guidelines

When submitting a pull request (PR) to the Phi-3 CookBook repository, please follow these guidelines:

- **Fork the Repository**: Always fork the repository to your own account before making changes.

- **Separate pull requests (PR)**:
  - Submit each type of change in its own pull request. For instance, bug fixes and documentation updates should go in separate PRs.
  - Typo fixes and minor documentation updates can be grouped into a single PR when appropriate.

- **Handle merge conflicts**: If your pull request has merge conflicts, update your local `main` branch to match the main repository before making changes.

- **Translation submissions**: When submitting a translation PR, ensure that the translation folder contains translations for all files in the original folder.

### Translation Guidelines

> [!IMPORTANT]
>
> When translating content in this repository, do not use machine translation. Only contribute translations for languages in which you are proficient.

If you are fluent in a non-English language, you can assist by translating the content. To ensure your translation is properly integrated, follow these steps:

- **Create translation folder**: Navigate to the relevant section folder and create a translation folder for the language you’re contributing to. For example:
  - For the introduction section: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - For the quick start section: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Follow this pattern for other sections (03.Inference, 04.Finetuning, etc.).

- **Update relative paths**: While translating, adjust the folder structure by adding `../../` to the beginning of relative paths in markdown files to ensure links work correctly. For example, update as follows:
  - Change `(../../imgs/01/phi3aisafety.png)` to `(../../../../imgs/01/phi3aisafety.png)`.

- **Organize your translations**: Place each translated file in the corresponding section's translation folder. For instance, if you’re translating the introduction section into Spanish, create the following structure:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Submit a complete PR**: Include translations for all files in a section within a single PR. Partial translations for a section will not be accepted. When submitting a translation PR, ensure the translation folder contains all files from the original folder.

### Writing Guidelines

To maintain consistency across all documents, adhere to these guidelines:

- **URL formatting**: Wrap all URLs in square brackets followed by parentheses, without extra spaces. For example: `[example](https://example.com)`.

- **Relative links**: Use `./` for links pointing to files or folders in the current directory, and `../` for those in a parent directory. For example: `[example](../../path/to/file)` or `[example](../../../path/to/file)`.

- **Not Country-Specific locales**: Ensure that links do not include country-specific locales. For example, avoid `/en-us/` or `/en/`.

- **Image storage**: Save all images in the `./imgs` folder.

- **Descriptive image names**: Name images clearly using English characters, numbers, and dashes. For example: `example-image.jpg`.

## GitHub Workflows

When you submit a pull request, the following workflows will run to validate the changes. Follow these instructions to ensure your pull request passes the checks:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

This workflow verifies that all relative paths in your files are correct.

1. To ensure your links work properly, perform the following tasks in VS Code:
    - Hover over any link in your files.
    - Press **Ctrl + Click** to follow the link.
    - If the link doesn’t work locally, it will trigger the workflow and fail on GitHub.

1. To fix this issue, perform these tasks using VS Code’s path suggestions:
    - Type `./` or `../`.
    - VS Code will display options based on your input.
    - Select the correct file or folder to ensure the path is accurate.

After correcting the relative path, save and push your changes.

### Check URLs Don't Have Locale

This workflow ensures that web URLs do not include country-specific locales. Since this repository is globally accessible, URLs should not contain country-specific locales.

1. To verify your URLs, perform the following checks:
    - Look for text like `/en-us/`, `/en/`, or any other language locale in the URLs.
    - If these are absent, you will pass the check.

1. To fix this issue, follow these steps:
    - Open the file highlighted by the workflow.
    - Remove the country locale from the URLs.

Once the country locale is removed, save and push your changes.

### Check Broken Urls

This workflow ensures that all web URLs in your files are functional and return a 200 status code.

1. To verify URL functionality, perform the following tasks:
    - Check the status of URLs in your files.

2. To fix broken URLs, follow these steps:
    - Open the file containing the broken URL.
    - Update the URL to the correct one.

After fixing the URLs, save and push your changes.

> [!NOTE]
>
> There may be instances where the URL check fails even though the link works. This could happen due to:
>
> - **Network restrictions:** GitHub Actions servers may face restrictions accessing certain URLs.
> - **Timeout issues:** URLs that take too long to respond may cause a timeout error in the workflow.
> - **Temporary server issues:** Occasional server downtime or maintenance can temporarily make a URL inaccessible during validation.

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.