# Removing Artifacts
rm -rfv build
rm -rfv dist
rm -rfv src/*.egg-info

# Build Package
python setup.py sdist bdist_wheel

# Install package for sandbox testing
pip install --no-cache-dir --force-reinstall dist/*.whl
