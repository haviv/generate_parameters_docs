# Authorization Request Initial Number Of Multiple Rows

**Technical Name:** AuthorizationRequestInitialNumberOfMultipleRows

**Category:** General - UI

**Default Value:**

**Impact Level:** Medium

**Description:**

The Authorization Request Initial Number Of Multiple Rows parameter controls the initial number of rows displayed during the authorization review process within the Pathlock Cloud GRC platform's user interface. This setting helps in managing the display of multiple authorization requests efficiently.

**Business Impact:**

Setting an appropriate initial number of multiple rows during authorization requests can significantly improve the user experience by ensuring that the interface is not overwhelmed with data. This can lead to quicker decision-making and a more streamlined workflow for managing security, risk, and compliance related to authorization reviews.

**Technical Impact when configured:**

When this parameter is configured, it directly impacts how many authorization requests are visible by default to the user conducting the review. A higher number of initial rows can be beneficial for comprehensive reviews, while a lower number might suit scenarios where simplicity and quick overviews are preferred.

**Example Scenario:**

An organization requires their security team to review a large number of authorization requests daily. By configuring the Authorization Request Initial Number Of Multiple Rows to a higher default value, the security team can efficiently review more requests at once, reducing the need for excessive scrolling or page navigation.

**Related Settings:**

- AuthorizationFieldHeader
- AuthorizationNa...

**Best Practices:** configure when needing to optimize for specific user interface experiences, avoid when default settings align with common user expectations.