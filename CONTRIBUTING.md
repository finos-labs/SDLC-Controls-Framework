# Contributing to the SDLC Common Controls Catalog

The SDLC Common Controls Catalog is licensed under the [Community Specification License 1.0](/governance-documents/Community_Specification_License-v1.md) and accepts contributions via git pull requests.  

Before contributing you must enroll as a participant in the Software Development Lifecycle Common Control Catalog project. Please see the [PARTICIPANTS.md](PARTICIPANTS.md) file for instructions.

## Contributing Issues

### Prerequisites

* [ ] Have you [searched for duplicates](https://github.com/finos-labs/SDLC-Controls-Framework/issues?utf8=%E2%9C%93&q=)?  A simple search for exception error messages or a summary of the unexpected behaviour should suffice.
* [ ] Are you running the latest version?
* [ ] Are you sure this is a bug or missing capability?

### Raising an Issue
* Create your issue [here](https://github.com/finos-labs/SDLC-Controls-Framework/issues/new).
* New issues contain two templates in the description: bug report and enhancement request. Please pick the most appropriate for your issue, **then delete the other**.
  * Please also tag the new issue with either "Bug" or "Enhancement".
* Please use [Markdown formatting](https://help.github.com/categories/writing-on-github/)
liberally to assist in readability.
  * [Code fences](https://help.github.com/articles/creating-and-highlighting-code-blocks/) for exception stack traces and log entries, for example, massively improve readability.

## Contributing Pull Requests (Code & Docs)
To make review of PRs easier, please:

 * Please make sure your PRs will merge cleanly - PRs that don't are unlikely to be accepted.
 * For code contributions, follow the existing code layout.
 * For documentation contributions, follow the general structure, language, and tone of the [existing docs](https://github.com/finos-labs/SDLC-Controls-Framework/wiki).
 * Keep commits small and cohesive - if you have multiple contributions, please submit them as independent commits (and ideally as independent PRs too).
 * Reference issues if your PR has anything to do with an issue (even if it doesn't address it).
 * Minimise non-functional changes (e.g. whitespace).
 * Ensure all new files include a header comment block containing the following text: * Licensed under the Creative Commons Attribution 4.0 International License. See http://creativecommons.org/licenses/by/4.0/.
 * If necessary (e.g. due to 3rd party dependency licensing requirements), update the [NOTICE file](https://github.com/finos-labs/SDLC-Controls-Framework/blob/main/NOTICE) with any new attribution or other notices.


### Commit and PR Messages

* **Reference issues, wiki pages, and pull requests liberally!**
* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move button left..." not "Moves button left...")
* Limit the first line to 72 characters or less
