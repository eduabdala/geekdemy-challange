
## ✅ Assumptions

- Students can add **any number** of programmes to the cart.
- Multiple instances of the **same programme category** can be added.
- Pro Membership is **optional**.
- If a student has both **Pro Membership** and a **coupon**, Pro Membership discounts are applied **before** the coupon.
- **B4G1** is automatically applied when **4 or more** programmes are in the cart, regardless of other coupons.
- **DEAL_G20** and **DEAL_G5** must be **explicitly applied** using `APPLY_COUPON`.
- If B4G1 is applicable (i.e., 4+ programmes), it will be used **even if another coupon was applied**.
- If **multiple coupons** are applied, the **best eligible one** is used (unless B4G1 overrides them due to quantity).

### 💡 Coupon Precedence Example

- If a student applies both `DEAL_G20` and `DEAL_G5`, and the subtotal is ₹10,000 or more, `DEAL_G20` is applied.
- If a student applies both `DEAL_G20` and `DEAL_G5` with **4 or more programmes**, `B4G1` is automatically used and the others are ignored.

---