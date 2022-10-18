#Ques 1
SUB1 <- sample(1:100,20)
SUB2 <- sample(1:100,20)
SUB3 <- sample(1:100,20)
MARKS <- data.frame(SUB1,SUB2,SUB3)

#Ques 1(a)
total_marks <- SUB1+SUB2+SUB3
#Ques 1(b)
MARKS <- cbind(MARKS,total_marks)
#Ques 1(c)
st.err <- function(x){
  return (sd(x)/sqrt(length(x)))
}
apply(MARKS,2,st.err)
#Ques 1(d)
MARKS$SUB1 <- MARKS$SUB1 + 0.25
MARKS$SUB2 <- MARKS$SUB2 + 0.25
MARKS$SUB3 <- MARKS$SUB3 + 0.25

#Ques 2
V1 <- SUB1
V2 <- SUB2
V3 <- SUB3
V_list <- list(V1,V2,V3)
lapply(V_list,sum)

#Ques 3
Total_SUM <- sapply(V_list,sum)

#Ques 4
sapply(V_list,function(x) x^2)

#Ques 5
I <- rep(1:4,each=5)
MARKS <- cbind(MARKS,I)
tapply(MARKS$SUB1,MARKS$I,mean)
tapply(MARKS$SUB1,MARKS$I,sd)

#Ques 6
f <- function(x,y){
  return (x/y)
}
mapply(f,V1,V2)

#Ques 7
#Find mean of all columns in seatbelts
apply(Seatbelts,2,mean)
