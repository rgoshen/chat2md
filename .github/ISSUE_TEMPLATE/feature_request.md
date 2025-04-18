# Feature Request

name: Feature Request
description: Suggest an idea or enhancement for chat2md
labels: [enhancement]
body:

- type: textarea
  id: proposal
  attributes:
  label: Describe the feature
  description: What would you like to see added or changed?
  placeholder: "I’d like chat2md to..."
  validations:
  required: true

- type: textarea
  id: rationale
  attributes:
  label: Why is this feature useful?
  description: How would this improve your workflow or others’?
  placeholder: "This would help because..."

- type: textarea
  id: context
  attributes:
  label: Any other context?
  placeholder: Screenshots, related issues, or anything else.
