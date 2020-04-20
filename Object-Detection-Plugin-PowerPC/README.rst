pl-objectdetection
================================

.. image:: https://badge.fury.io/py/objectdetection.svg
    :target: https://badge.fury.io/py/objectdetection

.. image:: https://travis-ci.org/FNNDSC/objectdetection.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/objectdetection

.. image:: https://img.shields.io/badge/python-3.5%2B-blue.svg
    :target: https://badge.fury.io/py/pl-objectdetection

.. contents:: Table of Contents


Abstract
--------

An app to ...


Synopsis
--------

.. code::

    python objectdetection.py                                           \
        [-v <level>] [--verbosity <level>]                          \
        [--version]                                                 \
        [--man]                                                     \
        [--meta]                                                    \
        <inputDir>
        <outputDir> 

Description
-----------

``objectdetection.py`` is a ChRIS-based application that...

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

    pip install objectdetection

and run with

.. code:: bash

    objectdetection.py --man /tmp /tmp

to get inline help. The app should also understand being called with only two positional arguments

.. code:: bash

    objectdetection.py /some/input/directory /destination/directory


Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

To run using ``docker``, be sure to assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``. *Make sure that the* ``$(pwd)/out`` *directory is world writable!*



Thus, getting inline help is:

.. code:: bash
    
    mkdir in out && chmod 777 out
    docker run --security-opt label=type:nvidia_container_t 
                -v $(pwd)/in:/incoming:z -v $(pwd)/out:/outgoing:z 
                docker.io/fnndsc/pl-objectdetection_moc_ppc64 
                objectdetection.py 
                /incoming /outgoing

Examples
--------
(assume that after building the image id is 72607209203a)

.. code:: bash
    
    mkdir in out && chmod 777 out
    docker run --security-opt label=type:nvidia_container_t 
                -v $(pwd)/in:/incoming:z -v $(pwd)/out:/outgoing:z 
                docker.io/fnndsc/pl-objectdetection_moc_ppc64 
                objectdetection.py 
                /incoming /outgoing




