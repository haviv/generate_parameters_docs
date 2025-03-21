# Use Validity Date As Deleted

**Technical Name:** UseValidityDateAsDeleted

**Category:** User Management

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

This parameter controls whether the validity date of a user is used to determine if the user should be considered as deleted within the Pathlock Cloud GRC platform. This feature plays a critical role in scenarios where managing user lifecycle and access must accurately reflect the user's current status without physically deleting user records from the system.

**Business Impact:**

Enabling this parameter ensures that users who have surpassed their validity date are automatically treated as deleted. This is crucial for maintaining compliance and minimizing security risks by preventing outdated or unauthorized access. Additionally, it helps businesses streamline user lifecycle management without the need for manual user deletion processes.

**Technical Impact when configured:**

When configured, this parameter dynamically alters the treatment of user records based on their validity date. It efficiently manages user access permissions by auto-declaring users as inactive or deleted when their validity expires. This results in a more secure and compliant environment, as it reduces the potential for unauthorized access by outdated user accounts.

**Example Scenario:**

A company utilizes the Pathlock Cloud GRC platform for managing their SAP user accounts. They have several temporary contractors who are given access to their system for a fixed duration. By enabling `UseValidityDateAsDeleted`, the system automatically restricts access for these contractors once their contract ends, thereby eliminating the need for manual intervention to remove their access rights, enhancing security and compliance with internal access policies.

**Related Settings:** N/A

**Best Practices:** 

- **Configure when:** Managing user access in a dynamic environment where user statuses frequently change, such as contractors with fixed-term access or employees on temporary assignments.
  
- **Avoid when:** User accounts require continuous manual review or in scenarios where automatic changes to user status could disrupt business operations.