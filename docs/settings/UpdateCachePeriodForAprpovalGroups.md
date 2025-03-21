# Update Cache Period For Approval Groups

**Technical Name:** UpdateCachePeriodForApprovalGroups

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Update Cache Period For Approval Groups parameter controls the duration for which approval group data remains cached before an update is required. By adjusting this period, organizations can balance between performance and data freshness, ensuring that decision-makers always operate with the most current information available.

**Business Impact:**

Configuring the cache period impacts how promptly changes in approval group assignments are recognized by the system. A shorter cache period enhances the responsiveness to changes, thereby reducing the risk of unauthorized access or delayed inclusion in critical approval workflows. Conversely, a longer period may benefit system performance but at a potential cost to compliance and security responsiveness.

**Technical Impact when configured:**

- **Increased System Performance:** A longer cache duration means less frequent data refreshes, which can reduce the load on databases and network resources.
- **Data Freshness:** A shorter cache duration ensures that updates to approval groups are promptly reflected, minimizing the risk of decisions being made based on outdated information.

**Examples Scenario:**

An organization implements a policy requiring approval for high-risk activities. The Update Cache Period For Approval Groups is set to ensure that any changes to approval groups—such as adding a new department head as an approver—are reflected within an acceptable time frame. This setup ensures that all high-risk activities are reviewed by the appropriate personnel, adhering to compliance requirements.

**Related Settings:**

- AlwaysShowUpdateButtonForRoleReview

**Best Practices:** 

- **Configure when**: Frequent changes occur within approval groups, or compliance mandates require up-to-date approvals for specific processes.
- **Avoid when**: The organization has stable approval groups with infrequent changes, and system performance is a priority over data freshness.