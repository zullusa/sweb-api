from typing import Any
from base import BaseAPI


class PayAPI(BaseAPI):
    def is_autopayment_enable(self) -> Any:
        return self._call("isAutopaymentEnable")

    def get_pay_recommendations(self, add_balance_recommendations: bool = False) -> Any:
        return self._call("getPayRecommendations", {"addBalanceRecommendations": add_balance_recommendations})

    def get_recommendation_total_cost(self) -> int:
        return self._call("getRecommendationTotalCost")

    def get_upcoming_payments_vh(self) -> Any:
        return self._call("getUpcomingPaymentsVh")

    def change_deferment(self, turn_on: bool) -> int:
        return self._call("changeDeferment", {"turnOn": turn_on})

    def get_remains_date(self) -> str:
        return self._call("getRemainsDate")

    def get_remains_days(self) -> int:
        return self._call("getRemainsDays")

    def get_balance(self) -> Any:
        return self._call("getBalance")

    def get_active_reserves(self) -> Any:
        return self._call("getActiveReserves")
