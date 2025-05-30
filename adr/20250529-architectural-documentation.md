# Architectural Documentation

## Context
A method to easily collaborate on architectural design is required.  Design artifacts must be stored, tracked and easily publishable to other formats required for easy review by required stakeholders.

## Decision
Architectural design artifacts will be stored in a git repository, where possible as text or declarative code.

## Rationale
Source controlling documentation artifacts will allow for easy publishing of the content using automation pipelines.  Using text or declarative code will allow for easy review and tracking of design artifacts.  Binary formats should be discouraged as they are more difficult to review in terms of changes, however if a design artifact must be manually drawn, and it adds value to a design, then it should be included.

Design artifacts such as ADRs (architectural decision records), C4 diagrams (as code) and Wardley maps (as code) can be easily transformed and published using simple pipelines using open tools and APIs.  Regulatory requirements around collation of documentation can be easily automated, standardised and tracked.

## Status
Proposed

## Consequences
Architectural design artifacts such as ADRs (architectural decision records), C4 diagrams, Warley maps can be published to confluence, linked to work items, be formatted and collated for technical documentation.
