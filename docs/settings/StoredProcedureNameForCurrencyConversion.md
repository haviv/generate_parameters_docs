**Stored Procedure Name For Currency Conversion**

**Technical Name:** StoredProcedureNameForCurrencyConversion

**Category:** Configuration

**Default Value:** =convertCurrency($$Currency_Field$$,$$Conversion_Target_Currency$$,$$Conversion_Date$$)

**Impact Level:** Medium

**Description:** This parameter defines the stored procedure or expression used for currency conversion within the Pathlock Cloud GRC platform. It specifies how currency fields should be converted to a target currency on a given conversion date.

**Business Impact:** Proper configuration of this parameter ensures accurate financial reporting and compliance across different currencies, which is crucial for multinational corporations managing operations in various countries with different currencies.

**Technical Impact when configured:** Configuring this parameter correctly ensures that financial data, metrics, and reports reflect the true economic value by accounting for currency fluctuations over time. This conversion mechanism supports decision-making processes and compliance with international financial reporting standards.

**Example Scenario:** An organization operates in both the US and the UK. Financial transactions occurring in British Pound (GBP) need to be converted to US Dollar (USD) for consolidated financial reporting. By setting up this parameter correctly, all GBP transactions are automatically converted to USD based on the specified conversion rate and date, ensuring accurate financial statements.

**Related Settings:** 

- `Currency_Field` - Specifies the field that contains the currency amount to be converted.
- `Conversion_Target_Currency` - Defines the target currency to which the original currency amount will be converted.
- `Conversion_Date` - The date on which the conversion rate is applicable.

**Best Practices:** configure when planning to perform detailed financial analysis across multiple currencies. Avoid configuring this parameter without understanding the correct syntax and expected values to prevent incorrect currency conversion and potential financial discrepancies.