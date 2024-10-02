import nox
from .nox_utils import PY_VERSIONS, PDM_VER


## Run pytest with xdist, allowing concurrent tests
@nox.session(python=PY_VERSIONS, name="tests")
def run_tests(session: nox.Session):
    session.install(f"uv")
    session.run("uv", "pip", "install", ".")

    print("Running Pytest tests")
    session.run(
        "pytest",
        "-n",
        "auto",
        "--tb=auto",
        "-v",
        "-rsXxfP",
    )
