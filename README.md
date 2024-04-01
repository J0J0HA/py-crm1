# ``crm1`` Python package

This package is a Python implementation of the CRM-1 specification.

You can find the specification [here](https://github.com/CRModders/CRM-1/).

## Installation

You can install the package using pip:

```bash
pip install crm1
```

## Usage

```python
"""Usage example for the crm1 module."""

from crm1 import Repository, RepositoryPool, autorepo, utils

repo1 = Repository("https://crm-repo.jojojux.de/repo.json")
repo2 = "https://repo.crmodders.dev/repository.hjson"

pool = RepositoryPool()
pool.add_repository(repo1)
pool.add_repository(repo2)

repos = autorepo.get_all_repos()
pool2 = utils.make_pool(repos)

mod = pool.get_mod("dev.crmodders.flux")
print(mod.meta.name)

mod2 = pool.get_mod("com.nikrasoff.seamlessportals")

for dep in mod2.depends:
    dep.id = "dev.crmodders.flux"
    print(dep.mod)
    print(dep.resolve(pool))
    print(dep.mod.meta.name)

```

Everything is typed and documented, so you can use your IDE's autocomplete and documentation features to explore the functionality of the package.

## License

This package is licensed under the MIT license. You can find the full license text in the [LICENSE](LICENSE) file.
