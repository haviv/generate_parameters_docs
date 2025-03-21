# Authorization Request Comments Textbox Number Of Rows

**Technical Name:** AuthorizationRequestCommentsTextboxNumberOfRows

**Category:** General - UI

**Default Value:** 5

**Impact Level:** Medium

**Description:**

This parameter controls the initial number of visible rows in the comments textbox within the authorization request module. It is designed to enhance usability by adjusting the textbox size based on user preference or screen size.

**Business Impact:**

Adjusting this value impacts how users interact with the authorization request forms. A properly sized textbox can improve the user experience by eliminating the need for excessive scrolling, making it easier for users to review or input their comments. This can lead to faster processing of authorization requests and improved accuracy in communication.

**Technical Impact when configured:**

When configured, this parameter directly affects the user interface of the Pathlock Cloud GRC platform, specifically within the authorization request workflow. It determines the initial display size of the comments input field, potentially improving or hindering user interaction based on the configured value.

**Examples Scenario:**

- **Scenario 1:** If the platform is primarily used on devices with large screens, increasing the default value can ensure that users can see more of their comment at once, reducing the need to scroll and making review processes more efficient.

- **Scenario 2:** Conversely, if users primarily access the platform on smaller devices, reducing the number of rows can prevent the textbox from overwhelming the screen space, maintaining a balanced and user-friendly interface.

**Related Settings:**

- `AuthorizationRequestInitialNumberOfMultipleRows`
- `AuthorizationRequestAdditionalNumberOfMultipleRows`

**Best Practices:** 

- **Configure when:** Adjusting the number of visible rows can improve usability and efficiency for users who frequently work with authorization request comments. Consider the average screen size used by your organization when deciding on this value.
  
- **Avoid when:** Avoid setting a very high default on devices with smaller screens to prevent the comments textbox from dominating the user interface.