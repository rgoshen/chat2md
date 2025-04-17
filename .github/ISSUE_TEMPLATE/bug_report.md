# Bug Report

name: Bug Report
description: Report something that isn't working as expected
labels: [bug]
body:

- type: textarea
  id: what-happened
  attributes:
  label: What happened?
  description: Describe the bug in detail
  placeholder: Tell us what you saw...
  validations:
  required: true

- type: textarea
  id: expected
  attributes:
  label: What did you expect to happen?
  placeholder: Describe the expected behavior

- type: textarea
  id: steps
  attributes:
  label: Steps to Reproduce
  description: Be as specific as possible
  placeholder: | 1. Run `chat2md path/to/convo.json` 2. Look at the output 3. See the error

- type: input
  id: version
  attributes:
  label: chat2md version
  placeholder: "e.g. 0.1.0"
  validations:
  required: false
