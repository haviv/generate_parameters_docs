# Combination Max Systems For Display

**Technical Name:** CombinationMaxSystemsForDisplay

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the maximum number of systems that can be displayed in the Combination Systems user control. It helps in managing the visual representation of system combinations to the users, ensuring that the user interface remains uncluttered and the system's performance is optimized by limiting the number of systems displayed.

**Business Impact:**

Setting an appropriate value for this parameter can significantly impact the usability and performance of the Pathlock Cloud GRC platform from a managerial and auditing perspective. An excessively high value could lead to a cluttered display, making it difficult for users to efficiently analyze the data, while a value that is too low may restrict the visibility of critical system combination information required for effective decision-making.

**Technical Impact when configured:**

Proper configuration ensures a balance between usability and performance. It directly affects how information is presented to the user, potentially streamlining operations related to security, risk, and compliance by enabling or restricting visibility on the number of systems involved in any given risk or compliance scenario.

**Examples Scenario:**

- If the `CombinationMaxSystemsForDisplay` is set to a low value in an environment where users need to review multiple systems simultaneously for comprehensive SOD (Segregation of Duties) analysis, this might hinder their ability to perform an effective analysis.
- Setting this parameter to a high value in a densely populated Pathlock Cloud GRC environment could result in information overload, negatively affecting the user experience and system performance during compliance reporting.

**Related Settings:** 

None directly related from the analyzed code references.

**Best Practices:** 

- Configure this parameter based on the average number of system combinations commonly reviewed by the users.
- Avoid setting this value too high to prevent information overload and potential performance issues.
- Periodically review and adjust this setting as the organizational structure or Pathlock Cloud GRC usage evolves.