from ray.tune._structure_refactor import warn_structure_refactor
from ray.tune.search.hyperopt import *  # noqa: F401, F403

warn_structure_refactor(__name__, "ray.tune.search.hyperopt")
