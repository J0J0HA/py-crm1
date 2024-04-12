"""Usage example for the crm1 module."""

from crm1 import Repository, RepositoryPool, autorepo

# You can get a repository from a URL
repo1 = Repository.from_address("https://crm-repo.jojojux.de/repo.json")
# We have the helper funtions .from_address(address), .from_dict(data) and .from_hjson(raw_hjson) so you can create a repository from a dict or a URL.
# You can also create a repository from a RRRepository object, which is a dataclass that holds the raw data of a repository
repo2 = Repository.from_address("https://repo.crmodders.dev/repository.hjson")
repo3 = Repository.from_address(
    "https://codeberg.org/EmmaTheMartian/crm1-repo/raw/branch/main/repository.hjson"
)

# Now we create a pool and add the repositories to it
pool = RepositoryPool()
pool.add_repository(repo1)
pool.add_repository(repo2)

pool2 = RepositoryPool()
pool2.add_repository(repo3)

# Repo Dependencies are resolved automatically, so you can get a mod from a repository
# and it will automatically resolve the repositories it depends on
print(pool2.repositories.keys())

# You could also use the autorepo module to get all repositories known to the Autorepo at https://crm-repo.jojojux.de/repo_mapping.json
repos = autorepo.get_all_repos()
# You can also use the make_pool function to create a pool from a list of repositories
pool3 = RepositoryPool.make(repos)

# Now we can get a mod from the pool
mod = pool.get_mod("dev.crmodders.flux")
print(mod.meta.name)  # This will print "Flux API", the mods name

print(
    mod.meta.ext.changelog
)  # The mod.meta.ext attribute holds the CommonModExt object, which add typing and docs to commonly used fileds the mod.ext dict.
# The unknown fields are stored in the mod.meta.ext.others attribute, which is a dict.
# If you want to get the original mod.ext dict, you can use mod.original_ext.

# Now we load a different mod
mod2 = pool.get_mod("com.nikrasoff.seamlessportals")

# We can now iterate over the dependencies of the mod
for dep in mod2.depends:
    dep.id = "dev.crmodders.flux"  # Ignore this line, this is required because the de.jojojux.crm-repo repository has a bug, see https://github.com/J0J0HA/CRM-1-Autorepo/issues/6
    print(dep.mod)  # This will print None, because the dependency was not yet resolved
    # We can resolve the dependency by calling the resolve method and providing a repository or a pool to search in
    print(
        dep.resolve(pool)
    )  # This will print the mod object, as it is returned by the resolve method, but is also stored in the dependency object at dep.mod
    # We can now access the mod object from the dependency object
    print(
        dep.mod.meta.name
    )  # This will print the name of the mod, in this case "Flux API". If the dependency could not be resolved, the dep.mod attribute will still be None
