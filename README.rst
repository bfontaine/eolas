=====
Eolas
=====

**Eolas** is a toy language derived from a `@Maitre_Eolas’ Tweet`_. A few
people responded to the Tweet saying it was invalid code and it wouldn’t be
possible to write such program in any language due to obvious flaws like ``=``
for comparison and strings without quotes.

This project provides an interpreter for that language. It parses the original
program and evaluates it as intended.

.. _`@Maitre_Eolas’ Tweet`: https://twitter.com/Maitre_Eolas/status/830450153391849472

Install
-------

**Eolas** is distributed as a Python3 library and executable::

    pip install eolas

Note: you may need to use ``pip3`` instead of ``pip`` if your default
installation is Python 2.

Run
---

Run ``eolas --help`` to see all options. The interpreter reads from ``STDIN``
unless you give it a filename. You may also evaluate short programs using
``--eval "<your code>"``.

You can set the original memory using ``--set name=value``. Compare the results
when the interpreter is run on the original program::

    $ eolas code.eolas
    lose
    $ eolas --set 'avocat=Maitre Eolas' code.eolas
    Win

Specification
-------------

The original code block::

    {
    IF (avocat = Maitre Eolas)
    THEN (Result = Win)
    ELSE
    (Result = lose)
    return 0;
    }

In **Eolas**, a program is a suite of instructions wrapped in curly brackets.

Instructions
~~~~~~~~~~~~

**Eolas** has three instructions:

* ``IF (condition) THEN (instruction) ELSE (instruction)``: Usual if/then/else.
  The ``ELSE`` part is mandatory as well as parentheses everywhere. You can’t
  have more than one instruction in each part. The condition can be any
  expression.
* Assignment: assignments in **Eolas** work as expected, using the syntax
  ``name = value``. All variables are global and names may contain spaces.
* ``return code``: Interrupt the program with the given exit code.

A program may store its result in a special variable ``Result``. It’ll be
printed by the interpreter at the end.

Expressions
~~~~~~~~~~~

Only three value types are supported: integers, strings, and booleans. There is
no literal for booleans; they can only be obtained through comparison
operators. There’s only one such operator for now: ``=`` to check for equality.

The ``=`` operator is right-associative, so you can write code like this::

    { this_is_true = 42 = 42 }

Variables may contain spaces and evaluate to their string representation if
they’re not set. There is no other way to write strings, and as such empty
strings can’t be written.

Negative integers are not supported.
