# Contributing to Phi-3CookBook

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit [https://cla.microsoft.com](https://cla.microsoft.com).

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information read the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Cautions for creating issues

Please do not open GitHub issues for general support questions as the GitHub list should be used for feature requests and bug reports. This way we can more easily track actual issues or bugs from the code and keep the general discussion separate from the actual code.

## How to Contribute

### Pull Requests Guidelines

When submitting a pull request (PR) to the Phi-3 CookBook repository, please use the following guidelines:

- **Fork the Repository**: Always fork the repository to your own account before making your modifications.

- **Separate pull requests (PR)**:
  - Submit each type of change in its own pull request. For example, bug fixes and documentation updates should be submitted in separate PRs.
  - Typo fixes and minor documentation updates can be combined into a single PR where appropriate.

- **Handle merge conflicts**: If your pull request shows merge conflicts, update your local `main` branch to mirror the main repository before making your modifications.

- **Translation submissions**: When submitting a translation PR, ensure that the translation folder includes translations for all files in the original folder.

### Translation Guidelines

> **Important**
>
> When translating text in this repository, do not use machine translation. Only volunteer for translations in languages where you are proficient.

If you are proficient in a non-English language, you can help translate the content. Follow these steps to ensure your translation contributions are properly integrated, please use the following guidelines:

- **Create translation folder**: Navigate to the appropriate section folder and create a translation folder for the language you are contributing to. For example:
  - For the introduction section: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - For the quick start section: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Continue this pattern for other sections (03.Inference, 04.Finetuning, etc.)

- **Update relative paths**: When translating, adjust the folder structure by adding `../../` to the beginning of relative paths within the markdown files to ensure links work correctly. For example, change as following:
  - Change `(../../imgs/01/phi3aisafety.png)` to `(../../../../imgs/01/phi3aisafety.png)`

- **Organize your translations**: Each translated file should be placed in the corresponding section's translation folder. For example, if you are translating the introduction section into Spanish, you would create as following:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Submit a complete PR**: Ensure all translated files for a section are included in one PR. We do not accept partial translations for a section. When submitting a translation PR, make sure that the translation folder includes translations for all files in the original folder.

### Writing Guidelines

To ensure consistency across all documents, please use the following guidelines:

- **URL formatting**: Wrap all URLs in square brackets followed by parentheses, without any extra spaces around or inside them. For example: `[example](https://example.com)`.

- **Relative links**: Use `./` for relative links pointing to files or folders in the current directory, and `../` for those in a parent directory. For example: `[example](./path/to/file)` or `[example](../path/to/file)`.

- **Not Country-Specific locales**: Ensure that your links do not include country-specific locales. For example, avoid `/en-us/` or `/en/`.

- **Image storage**: Store all images in the `./imgs` folder.

- **Descriptive image names**: Name images descriptively using English characters, numbers, and dashes. For example: `example-image.jpg`.

## GitHub Workflows

When you submit a pull request, the following workflows will be triggered to validate the changes. Follow the instructions below to ensure your pull request passes the workflow checks:

- [Check Broken Relative Paths](#check-broken-relative-paths)
- [Check URLs Don't Have Locale](#check-urls-dont-have-locale)

> **Note**
>
> The current workflow is configured to use `pull_request_target`, which means it runs in the context of the `main` branch (the original repository you forked from) rather than your fork's branch. As a result, even if you correct the relative paths in your pull request, the workflow might still fail if there are incorrect paths in the `main` branch of the original repository.

### Check Broken Relative Paths

This workflow ensures that all relative paths in your files are correct.

1. To make sure your links are working properly, perform the following tasks using VS Code:
    - Hover over any link in your files.
    - Press **Ctrl + Click** to navigate to the link.
    - If you click on a link and it doesn't work locally, it will trigger the workflow and not work on GitHub.

1. To fix this issue, perform the following tasks using the path suggestions provided by VS Code:
    - Type `./` or `../`.
    - VS Code will prompt you to choose from the available options based on what you typed.
    - Follow the path by clicking on the desired file or folder to ensure your path is correct.

Once you have added the correct relative path, save and push your changes.

### Check URLs Don't Have Locale

This workflow ensures that any web URL doesn't include a country-specific locale. As this repository is accessible globally, it is important to ensure that URLs do not contain your country's locale.

1. To verify that your URLs don't have country locales, perform the following tasks:

    - Check for text like `/en-us/`, `/en/`, or any other language locale in the URLs.
    - If these are not present in your URLs, then you will pass this check.

1. To fix this issue, perform the following tasks:
    - Open the file path highlighted by the workflow.
    - Remove the country locale from the URLs.

Once you remove the country locale, save and push your changes.
