import setuptools
import re
from pathlib import Path

def get_version():
	version_file = Path(__file__).parent / "new_demo_app" / "__init__.py"
	with open(version_file) as f:
		content = f.read()
	match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', content)
	return match.group(1) if match else "0.0.1"

setuptools.setup(
	name="new_demo_app",
	version=get_version(),
	description="New Demo App for Frappe",
	author="Your Name",
	packages=setuptools.find_packages(),
	include_package_data=True,
	install_requires=[],
	zip_safe=False,
)
