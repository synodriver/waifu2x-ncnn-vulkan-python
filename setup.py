import sys
import os
import re

from skbuild import setup


def get_pyversion() -> str:
    return str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro)


def get_version() -> str:
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "waifu2x", "__init__.py")
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    result = re.findall(r"(?<=__version__ = \")\S+(?=\")", data)
    return result[0]


def get_dis():
    with open("README.markdown", "r", encoding="utf-8") as f:
        return f.read()


def main():
    dis = get_dis()
    setup(
        name="waifu2x",
        packages=['waifu2x'],
        version=get_version(),
        url="https://github.com/synodriver/waifu2x",
        keywords=["waifu2x"],
        description="waifu2x",
        long_description_content_type="text/markdown",
        long_description=dis,
        author="synodriver",
        license="GPLv3",
        python_requires=">=3.6",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Operating System :: OS Independent",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Topic :: Scientific/Engineering :: Image Processing",
            "Programming Language :: C",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: Implementation :: CPython"
        ],
        include_package_data=True,
        zip_safe=True,
        cmake_args=[
            "-DNCNN_VULKAN=ON",
            "-DNCNN_BUILD_TOOLS=OFF",
            "-DNCNN_BUILD_EXAMPLES=OFF",
            f'-DPYTHON_EXECUTABLE="{sys.executable}"',
            "-DPYBIND11_FINDPYTHON=OFF"]
        # f"DPYBIND11_PYTHON_VERSION='{get_pyversion()}'"],

    )


# 环境变量 VULKAN_SDK
if __name__ == "__main__":
    main()
