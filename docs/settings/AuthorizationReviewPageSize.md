# Authorization Review Page Size

**Technical Name:** AuthorizationReviewPageSize

**Category:** Authorization Review

**Default Value:** 

**Impact Level:** Medium

**Description:** 

The Authorization Review Page Size parameter is designed to manage the number of authorization review items displayed per page within the Pathlock Cloud GRC platform's Authorization Review sections. This parameter helps in customizing the view for better manageability and readability of authorization data.

**Business Impact:**

Modifying the Authorization Review Page Size can significantly impact how users interact with authorization review processes. A smaller page size may increase the number of pages but can make each page faster to load and easier to review, which is crucial during extensive audit reviews. Conversely, a larger page size can reduce the number of pages but may increase the load time per page, potentially lowering the efficiency of the review process in scenarios with vast amounts of authorization data.

**Technical Impact when configured:**

When the Authorization Review Page Size is configured, it directly affects the loading time of authorization review pages and the ease of navigation for users involved in the authorization review process. Adequate configuration of this parameter could lead to optimized performance and enhanced user experience within the authorization review workflow.

**Examples Scenario:**

- **Audit Preparation:** During periods of audit preparation, auditors require quick and efficient access to authorization data. Setting an appropriate page size allows auditors to navigate through authorization information effectively, ensuring a thorough and timely audit process.

**Related Settings:** 

- AuthorizationReviewForPositionChangeTitle

**Best Practices:** 

- **Configure when:** Adjusting the Authorization Review Page Size is particularly beneficial in scenarios of large-scale reviews where the default setting does not align with the organization's operational requirements or when there's feedback from users concerning the manageability of displayed data.
  
- **Avoid when:** Avoid setting the page size too high in environments where bandwidth or system performance is a concern, as this may negatively impact the load time and review efficiency. Similarly, if users are comfortable with the default setting and no operational inefficiencies are identified, it may be best to maintain the default configuration to avoid unnecessary changes.