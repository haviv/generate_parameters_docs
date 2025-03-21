**Authorization Review Show Fill Empty To Approve**

**Technical Name:** AuthorizationReviewShowFillEmptyToApprove

**Category:** Workflow

**Default Value:** Not provided

**Impact Level:** Medium

**Description:** 

This parameter controls whether to display or hide the option to mark empty fields as approved during an authorization review process. It is utilized within the authorization certification process, specifically in scenarios where a review of user details and permissions is required.

**Business Impact:** 

Enabling this setting can streamline the authorization review process by allowing reviewers to quickly approve items that do not have associated values, thereby focusing on entries that require attention. This can lead to a more efficient audit and compliance process by reducing the time spent on reviewing each entry manually.

**Technical Impact when configured:** 

When enabled, the system will display an option to automatically fill empty fields with an "approved" status during the authorization review process. If disabled, reviewers must manually review each entry, possibly increasing the time required for the review process.

**Examples Scenario:**

* A compliance officer is undergoing an audit of user permissions within the Pathlock GRC platform. For entries where no explicit permission is listed (i.e., the field is empty), the officer can opt to quickly approve these entries if this parameter is enabled, assuming lack of an explicit permission implies no access granted.

**Related Settings:** Not provided

**Best Practices:** 

- **Configure when** you have a large number of entries to review, and a significant portion of these entries typically do not require action. Enabling this setting can reduce manual effort and focus review on entries with explicit permissions.
  
- **Avoid when** comprehensive review of each entry is necessary, especially in highly regulated environments where even the absence of information may need explicit approval or review.