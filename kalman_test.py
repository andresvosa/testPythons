# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:42:35 2023

@author: kasutaja
"""


class KalmanFilter:
    def __init__(
        self,
        est_val,
        meas_val,
        est_err,
        meas_err,
    ):
        self.initial_val_estimated = est_val
        self.est_val = self.initial_val_estimated
        self.initial_estimation_err = est_err
        self.est_err = self.initial_estimation_err
        self.initial_measure_err = meas_err
        self.meas_err = self.initial_measure_err
        self.kg, self.est_val, self.est_err = self.calculate_next_state(
            meas_val, est_err, meas_err
        )

    def calculate_next_state(
        self,
        meas_val,
        est_err=None,
        meas_err=None,
    ):
        if est_err is None and meas_err is None:
            self.kg = self.est_err / (self.est_err + self.meas_err)
            self.est_err = (1 - self.kg) * (self.est_err)
            self.est_val = self.est_val + self.kg * (meas_val - self.est_val)
            return
        else:
            kg = est_err / (est_err + meas_err)
            est_err = (1 - kg) * (est_err)
            est_val = self.est_val + kg * (meas_val - self.est_val)
            return kg, est_val, est_err


def main():
    measured_values = [
        75.0,
        71.0,
        70.0,
        74,
        0,
    ]

    kf = KalmanFilter(68.0, measured_values[0], 2.0, 4.0)
    print(measured_values[0], kf.est_val, kf.kg, kf.est_err)

    for i in range(len(measured_values) - 2):
        kf.calculate_next_state(measured_values[i + 1])
        print(measured_values[i + 1], kf.est_val, kf.kg, kf.est_err)


if __name__ == "__main__":
    main()
