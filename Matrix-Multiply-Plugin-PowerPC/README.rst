pl-MatMultiply
================================

.. image:: https://badge.fury.io/py/matmultiply.svg
    :target: https://badge.fury.io/py/matmultiply

.. image:: https://travis-ci.org/FNNDSC/matmultiply.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/matmultiply

.. image:: https://img.shields.io/badge/python-3.5%2B-blue.svg
    :target: https://badge.fury.io/py/pl-matmultiply

.. contents:: Table of Contents


Abstract
--------

An app to ...


Synopsis
--------

.. code::

    python matmultiply.py                                           \
        [-v <level>] [--verbosity <level>]                          \
        [--version]                                                 \
        [--man]                                                     \
        [--meta]                                                    \
        <inputDir>
        <outputDir> 

Description
-----------

``matmultiply.py`` is a ChRIS-based application that...

Agruments
---------

.. code::

    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.

    [--version]
    If specified, print version number. 
    
    [--man]
    If specified, print (this) man page.

    [--meta]
    If specified, print plugin meta data.


Run
----

This ``plugin`` can be run in two modes: natively as a python package or as a containerized docker image.

Using PyPI
~~~~~~~~~~

To run from PyPI, simply do a 

.. code:: bash

    pip install matmultiply

and run with

.. code:: bash

    matmultiply.py --man /tmp /tmp

to get inline help. The app should also understand being called with only two positional arguments

.. code:: bash

    matmultiply.py /some/input/directory /destination/directory


Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

To run using ``docker``, be sure to assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``. *Make sure that the* ``$(pwd)/out`` *directory is world writable!*


.. code:: bash

    mkdir in out && chmod 777 out                                       \
    docker run  --security-opt label=type:nvidia_container_t            \   
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing          \
                fnndsc/pl-matrixmultiply_moc_ppc64                                \
                matmultiply.py                                          \
                -c 32,32,128                                            \
                /incoming /outgoing                 

Examples
--------
.. code:: bash

    docker run  --security-opt label=type:nvidia_container_t            \   
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing          \
                fnndsc/pl-matrixmultiply_moc_ppc64                                \
                matmultiply.py                                          \
                -c 32,32,128                                            \
                /incoming /outgoing   




