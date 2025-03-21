# User Percentage For Poc Data Upload

**Technical Name:** UserPercentageForPocDataUplaod

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter specifies the percentage of users selected for proof of concept (PoC) data uploads. It is used to filter a subset of user data in large datasets, enabling targeted analysis and testing without the need for full data migration. 

**Business Impact:**

Adjusting this parameter allows organizations to manage the scope of PoC testing, focusing on a representative sample of users. This can lead to more efficient, cost-effective testing, reducing the time and resources required for preliminary analysis and validation in the Pathlock Cloud GRC platform.

**Technical Impact when configured:**

When configured, this parameter directly influences the volume of user data processed and uploaded as part of PoC operations. It can impact the performance of data processing tasks, the accuracy of testing outcomes, and the overall resource utilization of the GRC platform.

**Example Scenario:**

- A company is implementing a new access control policy within the Pathlock Cloud GRC platform and wants to test its impact. Adjusting this parameter to 10% allows the organization to upload and test the policy against 10% of the user base, enabling them to gather insights and make necessary adjustments before a full rollout.

**Related Settings:** 

- Update Cache Period For Approval Groups
- Use Forbidden Combination With Schema Filter

**Best Practices:** 

- **Configure when:** Initiating a proof of concept that requires a concise, manageable subset of user data for accurate analysis. Ideal for preliminary testing in large organizations to ensure scalability and effectiveness of the GRC controls or policies.
  
- **Avoid when:** Full data migration and comprehensive testing are required. In such cases, adjusting this percentage to include a larger portion of user data, or not using this filter at all, may be more appropriate to ensure thorough testing and analysis.
