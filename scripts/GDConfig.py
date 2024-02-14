import attr
import yaml
from pathlib import Path
from dotenv import get_variables


@attr.s(auto_attribs=True, kw_only=True, eq=False)
class GDConfig:
    manifest_path: Path
    profile: str
    host: str
    workspace_id: str
    data_source_id: str
    token: str
    source_dir: str
    env: dict[str, str]

    @classmethod
    def load(cls, manifest_path: Path, profile_name: str = None):
        with open(manifest_path) as f:
            config = yaml.safe_load(f.read())

        secrets = get_variables(".env")

        if not profile_name:
            profile_name = config["default_profile"] if config["default_profile"] else "dev"

        profile = config["profiles"][profile_name]

        if not profile:
            raise AssertionError(f"Missing profile {profile_name} in {manifest_path} file")

        if profile["token"].startswith("$"):
            if profile["token"][1:] in secrets:
                profile["token"] = secrets[profile["token"][1:]]
            else:
                raise AssertionError(f"Missing {profile['token']} variable in .env file")

        return cls(
            manifest_path=manifest_path,
            profile=profile_name,
            host=profile["host"],
            workspace_id=profile["workspace_id"],
            data_source_id=profile["data_source_id"],
            token=profile["token"],
            source_dir=config["source_dir"],
            env=secrets,
        )
