from brewtils import Plugin, command
import pandas as pd


class WhoStatistics(object):

    # Simple command that just returns pong
    @command(description='Returns pong')
    def ping(self):
        return 'pong'

    # Returns statistics for <country> in <year>
    @command(description='Returns statistics for <country> in <year>')
    def get_stat(self, country, year):
        # Read the .csv file 'LifeExpectancyData.csv and store as a dataframe object
        rf = pd.read_csv('LifeExpectancyData.csv')
        # Find location of <country> and <year> in the dataframe
        stat = rf.loc[(rf['Country'] == country) & (rf['Year'] == year)]
        # Returns as a normal python list
        return stat.round().values.tolist()

    # Returns the latest statistics for <country>
    @command(description='Returns the latest statistics for <country>')
    def get_latest(self, country):
        rf = pd.read_csv('LifeExpectancyData.csv')
        # Store all data from <country> in the dataframe object
        stat = rf.loc[rf['Country'] == country]
        # Return latest and convert to python list (rounded values for easy of use)
        return stat.iloc[[0]].round().values.tolist()

    # Returns the average statistics for <country>
    @command(description='Returns the average statistics for <country>')
    def get_avg(self, country):
        # Read the csv file and store as a dataframe object
        rf = pd.read_csv('LifeExpectancyData.csv')
        # Store all data from <country>
        stat = rf.loc[rf['Country'] == country]
        # Extract all values from the dataframe and get average values using .mean()
        average_stat = stat[['Life expectancy', 'Adult Mortality', 'Infant deaths', 'Alcohol',
                             "Percentage expenditure", "Hepatitis B", "Measles", "BMI",
                             "Under-five deaths", "Polio", "Total expenditure", "Diphtheria",
                             "HIV/AIDS", "GDP", "Population", "Thinness 1-19 years",
                             "Thinness 5-9 years", "Income composition of resources", "Schooling"]].mean()
        # Return rounded values as a normal python list
        return average_stat.round().values.tolist()

    # Returns the average statistics for <region> in <year>
    @command(description='Returns the average statistics for <region> in <year>')
    def get_avg_region(self, region, year):
        rf = pd.read_csv('LifeExpectancyData.csv')
        # Read the 'countriesoftheworld.csv' and store as a dataframe
        rf_regions = pd.read_csv('countriesoftheworld.csv')
        # Adding the two dataframe objects to one
        df_merged = pd.merge(rf, rf_regions)
        # Extract all selected rows  in <region> and <year> and find average values
        stat = df_merged.loc[(df_merged['Region'] == region) & (df_merged['Year'] == year)]
        average_stat_region = stat[['Life expectancy', 'Adult Mortality', 'Infant deaths', 'Alcohol',
                                    "Percentage expenditure", "Hepatitis B", "Measles", "BMI",
                                    "Under-five deaths", "Polio", "Total expenditure", "Diphtheria",
                                    "HIV/AIDS", "GDP", "Population", "Thinness 1-19 years",
                                    "Thinness 5-9 years", "Income composition of resources", "Schooling"]].mean()
        # Return rounded numbers as a list
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