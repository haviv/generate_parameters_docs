# Enable Modern Style For Reviews

**Technical Name:** EnableModernStyleForReviews

**Category:** Configuration

**Default Value:** <Not specified in provided code references>

**Impact Level:** Medium

**Description:**

This parameter controls the application of a modern style to the review interfaces within the Pathlock Cloud GRC platform. When enabled, it updates the visual presentation of the Authorization Certifications and other relevant interfaces to a more contemporary aesthetic, enhancing user experience.

**Business Impact:**

Enabling the modern style for reviews can significantly improve the user experience, making it more intuitive and engaging for users to perform their compliance, risk management, and audit tasks. It could lead to increased efficiency in review processes and better user compliance with necessary procedures due to a more user-friendly interface.

**Technical Impact when configured:**

When this parameter is configured to enable the modern style:
- Grid styles within the “UserDetails.aspx”, among other interfaces, are visually updated to align with the modern aesthetic.
- Certain user controls and elements might show or hide based on the parameter's state, affecting the interface's overall layout and functionality.

**Examples Scenario:**

A GRC platform administrator wants to ensure that the review process is as efficient and user-friendly as possible for auditors and compliance officers. By enabling the modern style for reviews, they can provide a more intuitive interface, potentially reducing the time taken to complete reviews and making the process more engaging for users.

**Related Settings:**

- AuthorizationReviewCustomizeDetailsButtonText
- AuthorizationReviewShowFillEmptyToApprove
- AuthorizationReviewShowFillEmptyToDecline

**Best Practices:** configure when a more modern, user-friendly interface is desired to enhance user engagement and efficiency in review processes; avoid when the existing interface meets the organization’s needs or when users are accustomed to the current layout and might resist change.