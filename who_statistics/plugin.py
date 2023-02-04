from brewtils import Plugin, command
import pandas as pd


class WhoStatistics(object):

    @command(description='Returns pong')
    def ping(self):
        return 'pong'

    # Returns statistics for <country> in <year>
    @command(description='Returns statistics for <country> in <year>')
    def get_stat(self, country, year):
        rf = pd.read_csv('LifeExpectancyData.csv')
        stat = rf.loc[(rf['Country'] == country) & (rf['Year'] == year)]
        return stat.round().values.tolist()

    # Returns the latest statistics for <country>
    @command(description='Returns the latest statistics for <country>')
    def get_latest(self, country):
        rf = pd.read_csv('LifeExpectancyData.csv')
        stat = rf.loc[rf['Country'] == country]
        return stat.iloc[[0]].round().values.tolist()

    # Returns the average statistics for <country>
    @command(description='Returns the average statistics for <country>')
    def get_avg(self, country):
        rf = pd.read_csv('LifeExpectancyData.csv')
        stat = rf.loc[rf['Country'] == country]
        average_stat = stat[['Life expectancy', 'Adult Mortality', 'Infant deaths', 'Alcohol',
                             "Percentage expenditure", "Hepatitis B", "Measles", "BMI",
                             "Under-five deaths", "Polio", "Total expenditure", "Diphtheria",
                             "HIV/AIDS", "GDP", "Population", "Thinness 1-19 years",
                             "Thinness 5-9 years", "Income composition of resources", "Schooling"]].mean()
        return average_stat.round().values.tolist()

    # Returns the average statistics for <region> in <year>
    @command(description='Returns the average statistics for <region> in <year>')
    def get_avg_region(self, region, year):
        rf = pd.read_csv('LifeExpectancyData.csv')
        rf_regions = pd.read_csv('countriesoftheworld.csv')
        df_merged = pd.merge(rf, rf_regions)
        stat = df_merged.loc[(df_merged['Region'] == region) & (df_merged['Year'] == year)]
        average_stat_region = stat[['Life expectancy', 'Adult Mortality', 'Infant deaths', 'Alcohol',
                                    "Percentage expenditure", "Hepatitis B", "Measles", "BMI",
                                    "Under-five deaths", "Polio", "Total expenditure", "Diphtheria",
                                    "HIV/AIDS", "GDP", "Population", "Thinness 1-19 years",
                                    "Thinness 5-9 years", "Income composition of resources", "Schooling"]].mean()
        return average_stat_region.round().values.tolist()


def main():
    client = WhoStatistics()

    plugin = Plugin(
        client=client,
        name="who",
        version="1.0.2",
        description="Plugin to get various countries health information",
        bg_host="localhost",
        bg_port="2337",
        ssl_enabled=False,
    )
    plugin.run()


if __name__ == "__main__":
    main()