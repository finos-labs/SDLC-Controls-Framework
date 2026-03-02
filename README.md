![badge-labs](https://user-images.githubusercontent.com/327285/230928932-7c75f8ed-e57b-41db-9fb7-a292a13a1e58.svg)

# SDLC Controls Framework

The purpose of this working group is to establish a common controls catalogue for software governance across financial institutions to increase reuse, reduce toil and provide additional clarity through consistency.

This repository contains the documentation and website, generated via Jekyll.


## Running locally

### Using Docker (recommended)

With Docker running, use the Makefile targets:

```sh
make run    # Serve the site at http://localhost:4000
make build  # Build the site without serving
make stop   # Stop the running dev server
make clean  # Remove generated _site and cache
make help   # Show all available targets
```

### Using Ruby

You will need Ruby and `bundle` installed, then run the site locally:

```sh
cd docs
bundle install
jekyll serve
```

Either way, view the site at http://localhost:4000.


## License

Copyright © 2025 Fintech Open Source Foundation

This work is licensed under a [Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

SPDX-License-Identifier: [CC BY 4.0](https://spdx.org/licenses/CC-BY-4.0.html).
