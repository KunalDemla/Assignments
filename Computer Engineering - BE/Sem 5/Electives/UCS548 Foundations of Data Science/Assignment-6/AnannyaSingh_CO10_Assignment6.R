library("gapminder")
aggregate( ~ continent, gapminder, median)
library("dplyr")
#1.1
gapminder %>% 
  group_by(continent) %>% 
  summarize(n=n_distinct(country))
#1.2
gapminder %>%
  filter(continent == "Europe" & year == 1997) %>%
  arrange(gdpPercap) %>%
  head(1)
#1.3
gapminder %>%
  filter(year == 1982 | year == 1987) %>%
  group_by(continent) %>%
  summarize(mean_lifeExp = mean(lifeExp))
#1.4
gapminder %>%
  mutate(gdp = gdpPercap*pop) %>%
  group_by(country) %>%
  summarise(Total.GDP = sum(gdp)) %>%
  arrange(desc(Total.GDP)) %>%
  head(5)
#1.5
gapminder %>%
  filter(lifeExp >= 80) %>%
  select(country, lifeExp, year)
#1.6
gapminder %>%
  group_by(country) %>%
  summarise(cor = cor(lifeExp, gdpPercap)) %>%
  arrange(desc(abs(cor))) %>%
  head(10)
#1.7
gapminder %>%
  filter(continent != "Asia") %>%
  group_by(continent, year) %>%
  summarise(mean.pop = mean(pop)) %>%
  arrange(desc(mean.pop)) 
#1.8
gapminder %>%
  group_by(country) %>%
  summarize(sd.pop = sd(pop)) %>%
  arrange(sd.pop) %>%
  head(3)
#1.9
gapminder %>% 
  arrange(country, year) %>% 
  group_by(country) %>% 
  filter(pop < lag(pop) & lifeExp > lag(lifeExp))