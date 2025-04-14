# User story title: Supply-Task Correlation

## Priority: 50
Could have:
A feature that allows for the correlation of cleaning supplies to specific cleaning tasks so that when a mess is reported, the system can indicate the exact supplies needed to resolve the issue efficiently.

## Estimation: e.g. 2 days
Any notes on estimation:
* Aaron: 4 days
* Seth: 4 days
* Harrison: 5 days

## Assumptions (if any):
- There is a predefined mapping between cleaning tasks and the supplies typically required to address them.
- Both cleaning supplies and tasks are stored in the system with sufficient detail to enable correlation.
- The system can be updated as new tasks or supplies are added.

## Description:
A robust feature that links cleaning supplies with their associated cleaning tasks. When a task is reported (for example, a specific type of spill or mess), the system provides a ready reference to the exact supplies required, thereby streamlining the preparatory process for the cleaner.

Description-v1:
An interface integration that displays correlated cleaning supplies alongside the details of a cleaning task. This enables immediate identification of the supplies needed for efficient job execution.

## Tasks, see chapter 4:
- Define and store mapping rules between cleaning tasks and their required supplies.
- Develop UI components to display correlated supply information when viewing a task.
- Implement backend logic to fetch and establish these correlations dynamically.
- Integrate with the cleaning tasks repository to offer a seamless lookup.
- Test the correlation feature under various scenarios and edge cases.

# UI Design:
- A joint view or overlay that appears when a cleaning task is selected, listing corresponding cleaning supplies.
- Visual cues (such as icons or color highlights) to denote matched items.
- Consistent, clear layout that complements the tasks and inventory views.

# Completed:
(Not completed)
