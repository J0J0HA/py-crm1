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
