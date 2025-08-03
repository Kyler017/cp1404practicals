"""
CP1404/CP5632 Practical
Add tests for SilverServiceTaxi using assert and print.
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    test_taxi = SilverServiceTaxi("Test Limo", 100, fanciness=2)
    test_taxi.start_fare()
    test_taxi.drive(18)
    expected_fare = (18 * 1.23 * 2) + 4.50  # = 48.78

    print(f"Expected fare: ${expected_fare:.2f}")
    print(f"Actual fare:   ${test_taxi.get_fare():.2f}")
    assert abs(test_taxi.get_fare() - expected_fare) < 0.01

    print("String output:")
    print(test_taxi)
    assert "plus flagfall" in str(test_taxi)


main()

