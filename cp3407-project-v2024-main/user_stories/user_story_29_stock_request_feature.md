# User story title: Stock Request Feature

## Priority: 25
Could have:
Implement a mechanism that enables users (employees or even the admin) to request additional stock. This ensures that when supply levels are low, timely replenishment can be initiated.

## Estimation: e.g. 1 day
Any notes on estimation:
* Aaron: 2 days
* Seth: x
* Harrison: 1 day

## Assumptions (if any):
- Only authorized users can submit a request.
- The current admin panel will be used to review and manage these requests.
- A notification system is already available or will be set up shortly.

## Description:
A feature within the platform that allows users to submit requests for additional supplies. The system will log these requests and provide a user-friendly interface for entering request details. Admins can review and act upon these submissions to keep the inventory adequately stocked.

Description-v1:
A form-based interface connected to the inventory system that enables employees to request more supplies. Each request is stored in the system, and administrators can then approve, reject, or follow up as needed.

## Tasks, see chapter 4:
- Create a user interface form for submitting stock requests.
- Develop backend endpoints to record and manage these requests.
- Integrate a notification mechanism to alert admins when a new request is submitted.
- Develop an admin interface for managing and tracking the status of these requests.

# UI Design:
- Implement a dedicated request panel accessible from the inventory dashboard.
- Include status indicators (e.g., pending, approved, completed) for each request entry.

# Completed:
(Not completed)
