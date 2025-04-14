# User story title: Multi-Factor Authentication

## Priority: 15
Must-Have
Justification: Very important to ensure security for both customer and service provider accounts. Regardless though
users should also be encouraged to create very strong passwords.

## Estimation:
* Aaron: 3 days
* Seth: 4 days
* Harrison: 5 Days

## Assumptions (if any):
* Sent via text/email

## Description:

Description-v1: As a customer/service provider, I want to provide an extra security layer to my account, so that 
I know my account is far less likely to be breached and personal information exposed.


## Tasks, see chapter 4.

1. Task 1: Allow users to enable multi-factor authentication when they register, Estimation XX days
2. Task 2: Generate a random number token when users log in, Estimation XX days
3. Task 3: Verify the entered details match what was generated, Estimation XX days
4. Task 4: Add option to enable/disable multi-factor authentication in profile settings, Estimation XX days


# UI Design:
** Registration Form Layout:
* Field: "Enable Multi-Factor Authentication" with a checkbox.
* Field: "Preferred Method" (Text/Email) dropdown.

** Login Page Layout:
* Step 1: Standard login fields (Username and Password).
* Step 2: Token input field for MFA.

** Profile Settings Layout:
* Field: "Enable/Disable Multi-Factor Authentication" toggle switch.
* Field: "Change Preferred Method" dropdown.

# Completed:
