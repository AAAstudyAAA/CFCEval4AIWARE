# Natural Language Toolkit: Utility functions
#
# Copyright (C) 2001-2020 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE

from itertools import chain

from tree_sitter import Language

AVAILABLE_LANGS = [
    "java",
    "javascript",
    "c_sharp",
    "php",
    "c",
    "cpp",
    "python",
    "go",
    "ruby",
    "rust",
]  # keywords available

AVAILABLE_LANGUAGES=[
    "c",
    "csharp",
    "cpp",
    "elixir",
    "erlang",
    "fortran",
    "go",
    "java",
    "js",
    "kotlin",
    "lua",
    "matlab",
    "objectivec",
    "php",
    "python",
    "r",
    "ruby",
    "rust",
    "scala",
    "swift"

]


def pad_sequence(
    sequence,
    n,
    pad_left=False,
    pad_right=False,
    left_pad_symbol=None,
    right_pad_symbol=None,
):
    """
    Returns a padded sequence of items before ngram extraction.
        >>> list(pad_sequence([1,2,3,4,5], 2, pad_left=True, pad_right=True,
        >>>      left_pad_symbol='<s>', right_pad_symbol='</s>'))
        ['<s>', 1, 2, 3, 4, 5, '</s>']
        >>> list(pad_sequence([1,2,3,4,5], 2, pad_left=True, left_pad_symbol='<s>'))
        ['<s>', 1, 2, 3, 4, 5]
        >>> list(pad_sequence([1,2,3,4,5], 2, pad_right=True, right_pad_symbol='</s>'))
        [1, 2, 3, 4, 5, '</s>']
    :param sequence: the source data to be padded
    :type sequence: sequence or iter
    :param n: the degree of the ngrams
    :type n: int
    :param pad_left: whether the ngrams should be left-padded
    :type pad_left: bool
    :param pad_right: whether the ngrams should be right-padded
    :type pad_right: bool
    :param left_pad_symbol: the symbol to use for left padding (default is None)
    :type left_pad_symbol: any
    :param right_pad_symbol: the symbol to use for right padding (default is None)
    :type right_pad_symbol: any
    :rtype: sequence or iter
    """
    sequence = iter(sequence)
    if pad_left:
        sequence = chain((left_pad_symbol,) * (n - 1), sequence)
    if pad_right:
        sequence = chain(sequence, (right_pad_symbol,) * (n - 1))
    return sequence


# add a flag to pad the sequence so we get peripheral ngrams?


def ngrams(
    sequence,
    n,
    pad_left=False,
    pad_right=False,
    left_pad_symbol=None,
    right_pad_symbol=None,
):
    """
    Return the ngrams generated from a sequence of items, as an iterator.
    For example:
        >>> from nltk.util import ngrams
        >>> list(ngrams([1,2,3,4,5], 3))
        [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
    Wrap with list for a list version of this function.  Set pad_left
    or pad_right to true in order to get additional ngrams:
        >>> list(ngrams([1,2,3,4,5], 2, pad_right=True))
        [(1, 2), (2, 3), (3, 4), (4, 5), (5, None)]
        >>> list(ngrams([1,2,3,4,5], 2, pad_right=True, right_pad_symbol='</s>'))
        [(1, 2), (2, 3), (3, 4), (4, 5), (5, '</s>')]
        >>> list(ngrams([1,2,3,4,5], 2, pad_left=True, left_pad_symbol='<s>'))
        [('<s>', 1), (1, 2), (2, 3), (3, 4), (4, 5)]
        >>> list(ngrams([1,2,3,4,5], 2, pad_left=True, pad_right=True, left_pad_symbol='<s>', right_pad_symbol='</s>'))
        [('<s>', 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, '</s>')]
    :param sequence: the source data to be converted into ngrams
    :type sequence: sequence or iter
    :param n: the degree of the ngrams
    :type n: int
    :param pad_left: whether the ngrams should be left-padded
    :type pad_left: bool
    :param pad_right: whether the ngrams should be right-padded
    :type pad_right: bool
    :param left_pad_symbol: the symbol to use for left padding (default is None)
    :type left_pad_symbol: any
    :param right_pad_symbol: the symbol to use for right padding (default is None)
    :type right_pad_symbol: any
    :rtype: sequence or iter
    """
    sequence = pad_sequence(sequence, n, pad_left, pad_right, left_pad_symbol, right_pad_symbol)

    history = []
    while n > 1:
        # PEP 479, prevent RuntimeError from being raised when StopIteration bubbles out of generator
        try:
            next_item = next(sequence)
        except StopIteration:
            # no more data, terminate the generator
            return
        history.append(next_item)
        n -= 1
    for item in sequence:
        history.append(item)
        yield tuple(history)
        del history[0]


def get_tree_sitter_language(lang: str) -> Language:
    """
    Get the tree-sitter language for a given language.
    :param lang: the language name to get the tree-sitter language for
    :return: the tree-sitter language
    """
    assert lang in AVAILABLE_LANGS, f"Language {lang} not available. Available languages: {AVAILABLE_LANGS}"

    try:
        if lang == "java":
            import tree_sitter_java

            return Language(tree_sitter_java.language())
        elif lang == "javascript":
            import tree_sitter_javascript

            return Language(tree_sitter_javascript.language())
        elif lang == "c_sharp":
            import tree_sitter_c_sharp

            return Language(tree_sitter_c_sharp.language())
        elif lang == "php":
            import tree_sitter_php

            try:
                return Language(tree_sitter_php.language())  # type: ignore[attr-defined]
            except AttributeError:
                return Language(tree_sitter_php.language_php())
        elif lang == "c":
            import tree_sitter_c

            return Language(tree_sitter_c.language())
        elif lang == "cpp":
            import tree_sitter_cpp

            return Language(tree_sitter_cpp.language())
        elif lang == "python":
            import tree_sitter_python

            return Language(tree_sitter_python.language())
        elif lang == "go":
            import tree_sitter_go

            return Language(tree_sitter_go.language())
        elif lang == "ruby":
            import tree_sitter_ruby

            return Language(tree_sitter_ruby.language())
        elif lang == "rust":
            import tree_sitter_rust

            return Language(tree_sitter_rust.language())
        else:
            assert False, "Not reachable"
    except ImportError:
        raise ImportError(
            f"Tree-sitter language for {lang} not available. Please install the language parser using `pip install tree-sitter-{lang}`."
        )
