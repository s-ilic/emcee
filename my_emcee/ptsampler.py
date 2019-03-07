# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import

try:
    from ptmy_emcee import Sampler as PTSampler
except ImportError:

    class PTSampler(object):

        def __init__(self, *args, **kwargs):
            raise ImportError(
                "The PTSampler from my_emcee has been forked to "
                "https://github.com/willvousden/ptmy_emcee, "
                "please install that package to continue using the PTSampler"
            )

__all__ = ["PTSampler"]
