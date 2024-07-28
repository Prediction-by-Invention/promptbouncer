#  Copyright (c) 2024. Prediction By Invention https://predictionbyinvention.com/
#
#  THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#  PARTICULAR PURPOSE, AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#  COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER
#  IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR
#  IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
from pathlib import Path

from src.promptbouncer.config.api import OPEN_API_YAML_SPEC_FILE


class FilePathUtil:
    """For handling file paths in the app."""

    def __init__(self):
        """Not needed in static utility class."""
        pass

    @staticmethod
    def app_root_path() -> str:
        script_path: Path = Path(__file__)
        return script_path.parent.parent.absolute().__str__()

    @staticmethod
    def repo_root_path() -> str:
        script_path: Path = Path(__file__)
        return script_path.parent.parent.parent.parent.absolute().__str__()

    @staticmethod
    def api_spec_path() -> str:
        return FilePathUtil.append_path_to_app_path(OPEN_API_YAML_SPEC_FILE)

    @staticmethod
    def append_path_to_app_path(path_str: str) -> str:
        app_root: str = FilePathUtil.app_root_path()
        return os.path.join(app_root, path_str)

    @staticmethod
    def append_path_to_repo_path(path_str: str) -> str:
        app_root: str = FilePathUtil.repo_root_path()
        return os.path.join(app_root, path_str)
