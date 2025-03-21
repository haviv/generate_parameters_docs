# Enable Central User Administration

**Technical Name:** EnableCUA

**Category:** User Management

**Default Value:**

**Impact Level:** High

**Description:**

Enables the Central User Administration (CUA) feature within the Pathlock Cloud GRC platform. This setting allows for centralized management of user roles and permissions across different systems or applications from a single point of control.

**Business Impact:**

Having CUA enabled ensures streamlined user management and governance, significantly reducing the overhead associated with managing users across multiple systems. It enhances compliance by ensuring consistent application of security policies and user roles, thereby minimizing the risk of unauthorized access and data breaches.

**Technical Impact when configured:**

When configured, the CUA setting allows administrators to efficiently allocate, update, or revoke user roles and permissions across all connected systems from the Pathlock platform. This centralized approach eliminates the need for managing users individually within each system, greatly improving operational efficiency and reducing the likelihood of errors.

**Examples Scenario:**

A company utilizes several different systems for their day-to-day operations, including ERP, CRM, and custom applications. Managing user permissions across these systems individually is time-consuming and prone to inconsistencies. By enabling CUA, the company can now centrally manage all user permissions from within the Pathlock platform, ensuring that users have appropriate access rights across all systems based on their role within the organization.

**Related Settings:**

- EnableApplyChangesFromAuthorizationSimulation

**Best Practices:** configure when,

- There is a need for centralized user role and permission management across multiple systems or applications.
- The organization requires a streamlined process for user management to ensure compliance and minimize security risks.

avoid when,

- The organization operates a single system or application, and the overhead of central management does not justify the setup and maintenance of CUA.