"""Usage example for the crm1 module."""

from crm1 import Repository, RepositoryPool, autorepo, make_pool

# You can get a repository from a URL
repo1 = Repository("https://crm-repo.jojojux.de/repo.json")
repo2 = "https://repo.crmodders.dev/repository.hjson"

# Now we create a pool and add the repositories to it
pool = RepositoryPool()
pool.add_repository(repo1)
# The RepositoryPool class can also take a string, a RRepository or a dict as a repository, it will automatically create a Repository object
# A RRRepository is a dataclass that holds the raw data of a repository
pool.add_repository(repo2)

# You could also use the autorepo module to get all repositories known to the Autorepo at https://crm-repo.jojojux.de/repo_mapping.json
repos = autorepo.get_all_repos()
# You can also use the make_pool function to create a pool from a list of repositories
pool2 = make_pool(repos)

# Now we can get a mod from the pool
mod = pool.get_mod("dev.crmodders.flux")
print(mod.meta.name)  # This will print "Flux API", the mods name

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
