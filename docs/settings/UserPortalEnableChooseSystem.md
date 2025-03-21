# User Portal Enable Choose System

**Technical Name:** UserPortalEnableChooseSystem

**Category:** Configuration

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

The UserPortalEnableChooseSystem parameter controls the visibility and operational aspect of system selection capabilities within the Pathlock Cloud GRC User Portal. When enabled, users have the ability to choose a system from a predefined list, enhancing user experience by allowing direct interaction with their authorized systems.

**Business Impact:**

Enabling this parameter empowers end-users with the flexibility to interact with different systems directly from the User Portal, potentially improving efficiency in tasks related to security, risk management, and compliance. It aids in streamlining user workflows by providing a centralized point of access for various systems.

**Technical Impact: when configured**

Upon enabling the UserPortalEnableChooseSystem parameter, the system selection option becomes available to users in the portal. This requires that systems are properly configured and available to be chosen, necessitating additional administrative oversight to ensure that only authorized systems are accessible.

**Examples Scenario:**

- A user needs to access multiple systems to perform their daily tasks. With UserPortalEnableChooseSystem enabled, the user can easily switch between systems through the User Portal, reducing the need for navigating away or logging in multiple times.

**Related Settings:** 

- ShowDeleteFromProfileInUserCard

**Best Practices:** 

- **Configure when:** You have a diverse set of users that require access to multiple systems through the User Portal and want to streamline their access.
  
- **Avoid when:** All users only ever need to access a single system, or where system selection could lead to potential security risks without proper configurations and checks in place.