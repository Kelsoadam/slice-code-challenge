# Slice Code Challenge

## Description

The purpose of this program is to develop a (hypothetical) robot that delivers 
pizza by assigning directional command on how to reach its destination, such as 
going North or East given a grid (where each point on the grid is one
house) and a list of points representing houses in need of pizza delivery,
return a list of instructions for getting Pizzabot to those locations and
delivering. The instructions will be fed into a String which will be printed at
the end, an example would be; for a delivery to positions 
```(1, 3)```and ```(4, 4)``` the  end result would be ``` ENNNDEEEND ```

## How to run

To run this program you can simply run the code from your IDE or CLI. The co-ordinates
for the houses can be change by editing the contents of the String at the top of the file 
called ```input_houses```. The current contents of this String is;
```
input_houses = ["5x5", "(0, 0)", "(1, 3)", "(4, 4)", "(4, 2)", "(4, 2)", "(0, 1)", "(3, 2)", "(2, 3)", "(4, 1)"]
```
The values for the desired house co-ordinates can be easily changed if revisions or additions to
the String are made while keeping the ```(x, y)``` format. While this process could be
streamlined by using stdin, the developer lacks the knowledge and experience with
running argument based CLI commands in their code and has made alterations to how the String is
input to compensate.

## Legacy Readme.md content

### Introduction

As part of Slice's commitment to reducing bias in the interview process, we're
asking you to complete a code challenge. The challenge is intended to be
respectful of your time, language- and platform-neutral, appropriate for
engineers of all skill levels, and (hopefully) fun. All challenges are stripped
of identifying information and judged against a rubric by two independent
reviewers. You can make the anonymization process easier for us by not
including your name in source files or documentation.

Slice engineers work predominantly in Ruby, Javascript, Python, Swift, and
Android Kotlin, but you're welcome to complete the challenge in the programming
language of your choice. If we believe we're not qualified to evaluate it,
we'll let you know.

If you successfully complete the challenge and agree to a formal interview,
we may ask you to pair-program with one of our engineers on an extension to
your submission as part of that process.

Please submit the solution to your challenge as a tarball, with clear
instructions on how to execute it.

## Rubric

Here's what we're looking for:

* _Correctness_. Does the code fulfill the requirements of the challenge?
* _Readability_. Is the code well-structured by the standards of the host
  language? Is it simple and clean? Does it reflect the domain of the problem?
* _Fit and polish_. Is there a README? A build script? Are there spelling
  errors or extraneous comments? How does it handle unspecified behavior?
* _Test coverage_. Not every developer writes tests, and that's okay. But we
  do. (Most of the time.)

## Challenge: Pizzabot (also see PDF)

As part of our continuing commitment to the latest cutting-edge pizza
technology research, Slice is working on a robot that delivers pizza. We call
it _(dramatic pause)_: Pizzabot. Your task is to instruct Pizzabot on how to
deliver pizzas to all the houses in a neighborhood.

In more specific terms, given a grid (where each point on the grid is one
house) and a list of points representing houses in need of pizza delivery,
return a list of instructions for getting Pizzabot to those locations and
delivering. An instruction is one of:

```
N: Move north
S: Move south
E: Move east
W: Move west
D: Drop pizza
```

Pizzabot always starts at the origin point, (0, 0). As with a Cartesian
plane, this point lies at the most south-westerly point of the grid.

Therefore, given the following input:

```sh
$ ./pizzabot "5x5 (1, 3) (4, 4)"
```

one correct solution would be:

```
ENNNDEEEND
```

In other words: move east once and north thrice; drop a pizza; move east thrice
and north once; drop a final pizza.

If you'd prefer to avoid stdin, or work predominantly in a platform that makes
it difficult to use, the equivalent solution expressed as an integration test is
just fine. The API is entirely up to you, as long as the test exercises
functionality that accepts and returns properly formatted strings:

```
assertEqual(pizzabot("5x5 (1, 3) (4, 4)"), "ENNNDEEEND")
```

There are multiple correct ways to navigate between locations. We do not take
optimality of route into account when grading: all correct solutions are good
solutions.

To complete the challenge, please solve for the following _exact input_:

```sh
5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)
```

Keep it simple, and have fun!
