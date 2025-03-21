# Campaigns Review Details Tab UAR

**Technical Name:** CampaignsReviewDetailsTabUAR

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The Campaigns Review Details Tab User Access Review (UAR) parameter controls the threshold settings for autocomplete suggestions presented in the User Access Review process within the Pathlock Cloud GRC platform. It specifically influences the limit and minimum prefix length required for autocomplete searches to trigger, optimizing the review process by offering quicker access to relevant user access records.

**Business Impact:**

Proper configuration of this parameter ensures an efficient and streamlined review process for auditors and managers. By setting appropriate limits, the system can balance performance and user convenience, directly impacting the organization's ability to maintain compliance and enforce access controls effectively.

**Technical Impact when configured:**

When configured, the parameter optimizes system performance during User Access Reviews by limiting the volume of data fetched and displayed. This results in faster response times and improves the user experience for administrators conducting access reviews, especially in large datasets.

**Examples Scenario:**

- **Scenario:** If the `AutoCompleteLimit` is set to a high number, users reviewing access permissions might experience slower response times due to the large amount of data being retrieved.
- **Mitigation:** Decreasing the `AutoCompleteLimit` value can help in fetching a more manageable subset of data, thus improving the system's response time during access reviews.

**Related Settings:**

- AutoCompleteLimit
- AutoCompleteMinimumPrefixLength

**Best Practices:** 

- **configure when:** you are experiencing slow response times during User Access Reviews or when users report difficulty in finding specific records using the autocomplete functionality.
- **avoid when:** the current settings do not negatively impact system performance or user experience, as unnecessary changes can inadvertently hinder the review process.