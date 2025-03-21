# Show Transaction Attribute1

**Technical Name:** ShowTransactionAttribute1

**Category:** Audit

**Default Value:** 

**Impact Level:** Medium

**Description:**

Enables the display of high-risk transactions within the activity grids. This parameter is crucial for enhancing visibility into transactions that may carry higher levels of risk and require additional scrutiny.

**Business Impact:**

Activating this parameter assists in prioritizing audit and review efforts by highlighting transactions of interest. It plays a significant role in risk management strategies by ensuring that high-risk transactions are readily identifiable, facilitating timely and effective responses.

**Technical Impact when configured:**

When enabled, the system dynamically generates columns in activity grids dedicated to high-risk transactions. This alters the presentation layer to include relevant data, augmenting the user's ability to identify and assess risk exposure within transactional data effectively.

**Example Scenario:**

A compliance officer wishes to review all high-risk transactions as part of their quarterly audit. By enabling ShowTransactionAttribute1, the officer can easily spot these transactions in the activity grid, streamlining the review process and ensuring no critical transaction is overlooked.

**Related Settings:** 

- ShowOnlyEndUsers
- ShowOnlyValidUsers
- ShowIsApprovedOnPageStart

**Best Practices:** Configure when conducting detailed audits or risk assessments to ensure high visibility of high-risk transactions. Avoid when unnecessary to prevent information overload and ensure the activity grid remains manageable for users.