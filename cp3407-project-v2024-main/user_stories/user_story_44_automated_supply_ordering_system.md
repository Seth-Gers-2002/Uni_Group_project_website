# User story title: Automated Supply Ordering System

## Priority: 40
Could have:
An automated module that locates required cleaning supplies based on the requested task and facilitates direct ordering, ensuring that the necessary supplies are acquired without manual intervention.

## Estimation: e.g. 2 days
Any notes on estimation:
* Aaron: x days
* Seth: x days
* Harrison: x days

## Assumptions (if any):
- The system is connected to supplier APIs or an in-house purchasing system.
- Reliable mapping exists between cleaning tasks and their required supplies.
- Security protocols and payment mechanisms are in place for handling orders.
- Automatic reordering can be triggered when correlated supplies fall below a threshold.

## Description:
An advanced feature that uses the correlation between cleaning tasks and supplies to automatically identify when supplies are low for a particular task, then trigger a reorder process. This ensures minimal downtime in operations and helps maintain a steady workflow by keeping supplies available when needed.

Description-v1:
A system that, upon detecting that a cleaning task has been requested and the supplies are insufficient, will automatically locate and order the necessary cleaning supplies directly into storage. This minimizes manual ordering and speeds up the replenishment process.

## Tasks, see chapter 4:
- Integrate with external supplier APIs or in-house ordering systems.
- Develop UI components for triggering and tracking automated orders.
- Implement backend logic to monitor inventory levels, correlate them with cleaning task needs, and initiate orders.
- Ensure security, authentication, and transaction logging for ordering processes.
- Test the automated ordering flow with simulated ordering scenarios.

# UI Design:
- A control panel area that shows ordering status, pending orders, and any automated triggers.
- Clear indicators and notifications for initiated and completed orders.
- A responsive and intuitive layout integrated with the supply tracker module.

# Completed:
(Not completed)
