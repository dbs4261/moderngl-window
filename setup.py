from setuptools import setup, find_namespace_packages

setup(
    name="moderngl_window",
    version="1.0.0",
    description="Easily create a window for ModernGL using the most popular window libraries",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/moderngl/moderngl_window",
    author="Einar Forselv",
    author_email="eforselv@gmail.com",
    packages=find_namespace_packages(include=['moderngl_window', 'moderngl_window.*']),
    keywords = ['moderngl', 'window', 'context'],
    license='MIT',
    platforms=['any'],
    python_requires='>=3.5',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Games/Entertainment',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: 3D Rendering',
        'Topic :: Scientific/Engineering :: Visualization',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
        'moderngl<6',
        'pyglet==1.4.0b1',
        'numpy>=1.16',
        'pyrr>=0.10.3',
    ],
    extras_require={
        "PySide2": ['PySide2>=5.13'],
        "pyqt5": ['PyQt5>=5.12'],
        "glfw": ['glfw>=1.7'],
        "PySDL2": ['PySDL2>=0.9.6'],
    },
    project_urls={
        'ModernGL': 'https://github.com/moderngl/moderngl',
    },
)
